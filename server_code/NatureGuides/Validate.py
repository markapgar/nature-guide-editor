
def is_blank(s):
  return not is_not_blank(s)

def is_not_blank(s):
  return bool(s and not s.isspace())