from bitcoin import *

# Sender's private key, public key, and address
sender_private_key = "5Kb8kLf9zgWQnogidDA76MzPL6TsZZY36hWXMssSzNydYXYB9KF"
sender_public_key = privtopub(sender_private_key)
sender_address = pubtoaddr(sender_public_key)

# Recipient's public key and address
recipient_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

# Amount to be transferred
amount = 0.01

# Create new transaction
tx = mksend(recipient_address, amount, sender_private_key, unspent)

# Broadcast transaction
broadcast(tx)