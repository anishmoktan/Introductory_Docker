import bcrypt

def hash_pw(password):
  hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
  return hashed#.decode("utf-8")

hased = hash_pw("anish")
print(hased)


def de_hash(hashed):
    return(bcrypt.hashpw(hashed.decode("utf-8"), bcrypt.gensalt())

print(de_hash(hased))