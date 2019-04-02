import claripy
import angr
import sys

def success(state):
	op = state.posix.dumps(sys.stdout.fileno())
	return "Good Job." in op

def fail(state):
	op = state.posix.dumps(sys.stdout.fileno())
	return "Try Again." in op

path = sys.argv[1]
project = angr.Project(path)
start_addr= 0x08048606
initial_state= project.factory.blank_state(addr=start_addr)
# for the 4 user inputs
pswd0=claripy.BVS('pswd0',8*8)
pswd1=claripy.BVS('pswd1',8*8)
pswd2=claripy.BVS('pswd2',8*8)
pswd3=claripy.BVS('pswd3',8*8)

# 8*8 --> always given in bits! Here for %8s we must have 8 char each of 1 byte
pswd0_addr=0xa29faa0
initial_state.memory.store(pswd0_addr,pswd0)
pswd1_addr=0xa29faa8
initial_state.memory.store(pswd1_addr,pswd1)
pswd2_addr=0xa29fab0
initial_state.memory.store(pswd2_addr,pswd2)
pswd3_addr=0xa29fab8
initial_state.memory.store(pswd3_addr,pswd3)

simulation=project.factory.simgr(initial_state)
simulation.explore(find=success,avoid=fail)
if simulation.found:
	sol=simulation.found[0]
	sol0= sol.se.eval(pswd0,cast_to=str)
	sol1=sol.se.eval(pswd1,cast_to=str)
	sol2=sol.se.eval(pswd2,cast_to=str)
	sol3=sol.se.eval(pswd3,cast_to=str)
	print(sol0,sol1,sol2,sol3)
else:
	print("No solution found!")





