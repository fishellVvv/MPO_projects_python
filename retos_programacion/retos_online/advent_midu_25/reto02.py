def manufacture_gifts(gifts_to_produce):
  return [gift.toy for gift in gifts_to_produce if isinstance(gift.quantity, int) and gift.quantity > 0 for _ in range(gift.quantity)]
