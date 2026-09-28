SKIP_USERS = {5, 10, 15}
STOP_TEST = 18

for user_id in range(1, 21):
    if user_id == STOP_TEST:
        print(f"Юзер {user_id}: тестирование прекращено.")
        break

    if user_id in SKIP_USERS:
        print(f"Юзер {user_id}: пропустить.")
        continue

    print(f"Юзер {user_id}: протестировано.")