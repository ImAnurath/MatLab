% Data
t_C = [13, 14, 17, 18, 19, 15, 13, 31, 32, 29, 27]';
t_F = [55, 58, 63, 65, 66, 59, 56, 87, 90, 85, 81]';

% Initial Parameters
initial_P_values = [1, 2, 3, 4]; % Different initial P values
theta_results = zeros(2, length(initial_P_values)); % To store results

% Loop over different initial P values
for idx = 1:length(initial_P_values)
    P = eye(2) * initial_P_values(idx); % Initial gain matrix
    theta = [0; 0]; % Initial guess for [k1; k2]

    % RLSE Algorithm
    for k = 1:length(t_C)
        Phi_k = [t_C(k), 1]'; % Regressor vector
        error = t_F(k) - Phi_k' * theta; % Prediction error
        K = P * Phi_k / (1 + Phi_k' * P * Phi_k); % Gain
        theta = theta + K * error; % Update parameters
        P = P - K * Phi_k' * P; % Update covariance matrix
    end

    % Store results for current P
    theta_results(:, idx) = theta;
end

% Using pinv() for comparison
X = [t_C, ones(length(t_C), 1)];
theta_pinv = pinv(X) * t_F;

% Display Results
disp('Estimated parameters using RLSE for different initial P values:');
disp(theta_results);

disp('Estimated parameters using pinv():');
disp(theta_pinv);

% Plotting the dependency of k1 and k2 on initial P
figure;
subplot(2, 1, 1);
plot(initial_P_values, theta_results(1, :), '-o', 'LineWidth', 2);
xlabel('Initial P Value');
ylabel('k1');
title('Dependency of k1 on Initial P');
grid on;

subplot(2, 1, 2);
plot(initial_P_values, theta_results(2, :), '-o', 'LineWidth', 2);
xlabel('Initial P Value');
ylabel('k2');
title('Dependency of k2 on Initial P');
grid on;

% Plotting data points and fitted line for pinv()
figure;
scatter(t_C, t_F, 'filled');
hold on;
t_F_pred = X * theta_pinv;
plot(t_C, t_F_pred, '-r', 'LineWidth', 2);
xlabel('t_C [Celsius]');
ylabel('t_F [Fahrenheit]');
title('Observed Data and Fitted Line');
legend('Data Points', 'Fitted Line (pinv())', 'Location', 'Best');
grid on;
