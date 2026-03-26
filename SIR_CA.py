import pygame
import numpy as np
import matplotlib.pyplot as plt

# --- States ---
S = 0
I = 1
R = 2

# --- Colors ---
col_S = (50, 100, 255)
col_I = (255, 50, 50)
col_R = (50, 255, 50)
col_grid = (30, 30, 60)

# --- Parameters ---
beta = 0.2   # infection probability
gamma = 0.05 # recovery probability


def mouse_to_cell(pos, cellsize):
    x, y = pos
    return y // cellsize, x // cellsize


def draw(surface, grid, cellsize):

    for state in [S, I, R]:
        rows, cols = np.where(grid == state)

        if state == S:
            color = col_S
        elif state == I:
            color = col_I
        else:
            color = col_R

        for r, c in zip(rows, cols):
            pygame.draw.rect(
                surface,
                color,
                (c * cellsize, r * cellsize, cellsize - 1, cellsize - 1),
            )


def update_sir(grid, beta, gamma):

    infected_neighbors = (
        np.roll(np.roll(grid == I, 1, 0), 1, 1) +
        np.roll(np.roll(grid == I, 1, 0), 0, 1) +
        np.roll(np.roll(grid == I, 1, 0), -1, 1) +
        np.roll(np.roll(grid == I, 0, 0), 1, 1) +
        np.roll(np.roll(grid == I, 0, 0), -1, 1) +
        np.roll(np.roll(grid == I, -1, 0), 1, 1) +
        np.roll(np.roll(grid == I, -1, 0), 0, 1) +
        np.roll(np.roll(grid == I, -1, 0), -1, 1)
    )

    new_grid = grid.copy()

    infect_prob = 1 - (1 - beta) ** infected_neighbors
    rand = np.random.rand(*grid.shape)

    new_grid[(grid == S) & (rand < infect_prob)] = I

    recover = (grid == I) & (np.random.rand(*grid.shape) < gamma)
    new_grid[recover] = R

    return new_grid


def init_grid(dimx, dimy):
    return np.zeros((dimy, dimx), dtype=int)


def main(dimx, dimy, cellsize):

    pygame.init()
    surface = pygame.display.set_mode((dimx * cellsize, dimy * cellsize))
    pygame.display.set_caption("Agent-Based SIR Model")

    clock = pygame.time.Clock()

    grid = init_grid(dimx, dimy)

    running = False
    step = False
    done = False

    # --- epidemic history ---
    S_hist = []
    I_hist = []
    R_hist = []

    while not done:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    done = True

                if event.key == pygame.K_SPACE:
                    running = not running

                if event.key == pygame.K_s:
                    step = True

                if event.key == pygame.K_c:
                    grid = init_grid(dimx, dimy)

            if event.type == pygame.MOUSEBUTTONDOWN:

                row, col = mouse_to_cell(event.pos, cellsize)

                if event.button == 1:   # left click → infect
                    if grid[row, col] == S:
                        grid[row, col] = I

                elif event.button == 3: # right click → recover
                    grid[row, col] = R

        surface.fill(col_grid)

        if running or step:

            grid = update_sir(grid, beta, gamma)
            step = False

            total = grid.size
            S_hist.append(np.sum(grid == S) / total)
            I_hist.append(np.sum(grid == I) / total)
            R_hist.append(np.sum(grid == R) / total)

        draw(surface, grid, cellsize)

        pygame.display.update()
        clock.tick(20)

    pygame.quit()
    pygame.display.quit()

    # --- Plot epidemic curves ---
    t = range(len(S_hist))

    plt.figure()

    plt.plot(t, S_hist, color=np.array(col_S)/255, label="Susceptible")
    plt.plot(t, I_hist, color=np.array(col_I)/255, label="Infected")
    plt.plot(t, R_hist, color=np.array(col_R)/255, label="Recovered")

    plt.xlabel("Time Step")
    plt.ylabel("Proportion of Population")
    plt.title("Agent-Based SIR Dynamics")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main(100, 70, 8)
