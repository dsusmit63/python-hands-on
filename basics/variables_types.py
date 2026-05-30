env = "prod"
no_of_instances = 1
cost_per_hour = 0.18272
isUp = True
openedPort = [22,80,443,5000,8080]
instanceObj = {
  "type": "t2.large",
  "cpu": 2,
  "ram": 16,
  "volume_size": 30,
  "volume_type": "gp3"
}
print(env);
print(type(env))
print(no_of_instances)
print(type(no_of_instances))
print(cost_per_hour)
print(type(cost_per_hour))
print(isUp)
print(type(isUp))
print(openedPort)
print(type(openedPort))
print(instanceObj)
print(type(instanceObj))