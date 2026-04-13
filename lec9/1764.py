N, M = map(int, input().split())

no_heard = set()
no_seen = set()

for i in range(N):
    no_heard.add(input().strip())
for i in range(M):
    no_seen.add(input().strip())


result = sorted(list(no_heard & no_seen))

print(len(result))
for name in result:
    print(name)
