import os
import pc_config

BOT_TOKEN = pc_config.token
admins = [
    340899114,
]

ip = os.getenv('ip')

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
