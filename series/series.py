def slices(series, length):
  if not series:
    raise ValueError('series cannot be empty string')

  if length <= 0:
    raise ValueError('length cannot be equal to or zero')
  
  if length > len(series):
      raise ValueError('length argument must be smaller than length series')

  start = 0
  slices = []
  while start <= (len(series) - length):
    slices.append(series[start:start+length])
    start += 1
  return slices