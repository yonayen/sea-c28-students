

def ack (m, n):
    """For ack -- values m and n are non-negative integers."""
	if m == 0:
		return (n + 1)
	elif m > 0 and n == 0:
		return ack(m - 1, 1)
	else:
		return ack(m - 1, ack(m, n - 1))