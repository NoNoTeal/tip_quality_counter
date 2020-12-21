def bruh (price, tax, qos): 
  price = float(price)
  tax = float(tax)
  qos = str(qos).lower()
  if not qos in ('good', 'ok', 'bad', 'no_tip') :
    raise Exception('QOS needs to be one of good, ok, or bad.')
    return;
  if qos is 'good':
    return (price + price * tax) + price * 0.2;
  if qos is 'ok':
    return (price + price * tax) + price * 0.15;
  if qos is 'bad':
    return (price + price * tax) + price * 0.05;
  if qos is 'no_tip':
    return (price + price * tax);
print(bruh(4, 0.47, 'no_tip'));
