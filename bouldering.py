def bouldering(energy):
    n = len(energy)
    if n == 0:
        return 0
    elif n == 1:
        return energy[0]
    
    # Initialize the dp array with 0 values
    dp = [0] * n
    # Base cases
    dp[0] = energy[0]
    dp[1] = energy[1]
    
    # Fill the dp array
    for i in range(2, n):
        dp[i] = energy[i] + min(dp[i-1], dp[i-2])
    
    # The result is the minimum energy used to reach the end
    return min(dp[n-1], dp[n-2])


if __name__ == "__main__":
    print(bouldering([5, 20, 25]))
    print(bouldering([5, 10, 20, 15, 5, 10, 15]))