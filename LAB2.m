% Define the function and range
f = @(x) (x + 1) ./ log((x + 2)); % Function definition from the list
x_range = linspace(1, 5, 500);    % Fine range for visualization
y_actual = f(x_range);            % True values of the function

% Define the approximation orders to test
orders = [2, 3, 5, 7, 9];

% Initialize storage for mean square errors
errors = zeros(size(orders));

% Plot the original function
figure;
plot(x_range, y_actual, 'k-', 'LineWidth', 1.5); hold on;
legend_entries = {'Original Function'};

% Loop through each approximation order
for i = 1:length(orders)
    n = orders(i); % Current order
    x_nodes = linspace(0, 1, n + 1); % Nodes for interpolation
    y_nodes = f(x_nodes);            % Evaluate function at nodes
    
    % Compute Lagrange Polynomial Coefficients
    coeffs = polyfit(x_nodes, y_nodes, n);
    
    % Evaluate the polynomial approximation
    y_approx = polyval(coeffs, x_range);
    
    % Calculate and store mean square error
    errors(i) = mean((y_actual - y_approx).^2);
    
    % Plot the approximation
    plot(x_range, y_approx, '--', 'LineWidth', 1.2);
    legend_entries{end+1} = sprintf('Lagrange Order %d', n);
end

% Finalize the plot
legend(legend_entries, 'Location', 'Best');
title('Function Approximation using Lagrange Polynomials');
xlabel('x'); ylabel('y');
grid on;

% Plot Mean Square Error
figure;
plot(orders, errors, 'bo-', 'LineWidth', 1.5, 'MarkerSize', 8);
title('Mean Square Error vs Approximation Order');
xlabel('Approximation Order');
ylabel('Mean Square Error');
grid on;
