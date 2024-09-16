# Building a simple CPU simulator in Python using MIPS instruction set architecture.
# Introduce pipelining and cache memory. 




class CPU_SIMULATOR:
    def __init__(self):
        self.registers = [0] * 32
        self.memory = [0] * 1024
        self.pc = 0
        self.running = False
        self.instructions = {
            "000000": self.add,
            "000001": self.sub,
            "000010": self.mul,
            "000011": self.div,
            "000100": self.and_,
            "000101": self.or_,
            "000110": self.xor,
            "000111": self.not_,
            "001000": self.lshift,
            "001001": self.rshift,
            "001010": self.load,
            "001011": self.store,
            "001100": self.jmp,
            "001101": self.jz,
            "001110": self.jnz,
            "001111": self.jgt,
            "010000": self.jlt,
            "010001": self.jeq,
            "010010": self.jne,
            "010011": self.jge,
            "010100": self.jle,
            "010101": self.mov,
            "010110": self.halt
        }
        self.pipeline = {
            "IF": None,
            "ID": None,
            "EX": None,
            "MEM": None,
            "WB": None
        }
        self.cache = {
            "L1": [None] * 4,
            "L2": [None] * 8
        }
        self.cache_hit = 0
        self.cache_miss = 0
        self.cache_access = 0
        self.cache_hit_rate = 0
        self.cache_miss_rate = 0
        self.cache_access_rate = 0

        def fetch(self):
            self.pipeline["IF"] = self.memory[self.pc]
            self.pc += 1
            
        def decode(self):
            self.pipeline["ID"] = self.pipeline["IF"]
            self.pipeline["IF"] = None
            
        def execute(self):
            self.pipeline["EX"] = self.pipeline["ID"]
            self.pipeline["ID"] = None
            opcode = self.pipeline["EX"][:6]
            self.instructions[opcode]()
         
        def memory_access(self):
            self.pipeline["MEM"] = self.pipeline["EX"]
            self.pipeline["EX"] = None
            opcode = self.pipeline["MEM"][:6]
            self.instructions[opcode]()
        
        def write_back(self):
            self.pipeline["WB"] = self.pipeline["MEM"]
            self.pipeline["MEM"] = None
            opcode = self.pipeline["WB"][:6]
            self.instructions[opcode]()
        
        def add(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] + self.registers[rt]
        
        def sub(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] - self.registers[rt]
            
        def mul(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] * self.registers[rt]
            
        def div(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] / self.registers[rt]
            
        def and_(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] & self.registers[rt]
            
        def or_(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] | self.registers[rt]
        
        def xor(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] ^ self.registers[rt]
         
        def not_(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            self.registers[rd] = ~self.registers[rs]
            
        def lshift(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] << self.registers[rt]
            
        def rshift(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.registers[rs] >> self.registers[rt]
            
        def load(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.registers[rd] = self.memory[self.registers[rs] + self.registers[rt]]
            
        def store(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            rt = int(instruction[16:21], 2)
            self.memory[self.registers[rs] + self.registers[rt]] = self.registers[rd]
            
        def jmp(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            self.pc = self.registers[rd]
            
        def jz(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] == 0:
                self.pc = self.registers[rd]
                
        def jnz(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] != 0:
                self.pc = self.registers[rd]
                
        def jgt(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] > 0:
                self.pc = self.registers[rd]
                
        def jlt(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] < 0:
                self.pc = self.registers[rd]
                
        def jeq(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] == 0:
                self.pc = self.registers[rd]
                
        def jne(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] != 0:
                self.pc = self.registers[rd]
                
        def jge(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] >= 0:
                self.pc = self.registers[rd]
                
        def jle(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            if self.registers[rd] <= 0:
                self.pc = self.registers[rd]
                
        def mov(self):
            instruction = self.pipeline["WB"]
            rd = int(instruction[6:11], 2)
            rs = int(instruction[11:16], 2)
            self.registers[rd] = self.registers[rs]
            
        def halt(self):
            self.running = False
            
        def run(self):
            self.running = True
            while self.running:
                self.fetch()
                self.decode()
                self.execute()
                self.memory_access()
                self.write_back()
                self.cache_access += 1
                self.cache_hit_rate = self.cache_hit / self.cache_access
                self.cache_miss_rate = self.cache_miss / self.cache_access
                print("Cache Hit Rate: ", self.cache_hit_rate)
                print("Cache Miss Rate: ", self.cache_miss_rate)
                print("Cache Access Rate: ", self.cache_access_rate)
                print("Cache Hit: ", self.cache_hit)
                print("Cache Miss: ", self.cache_miss)
                print("Cache Access: ", self.cache_access)
                print("Registers: ", self.registers)
                print("Memory: ", self.memory)
                print("PC: ", self.pc)
                print("Pipeline: ", self.pipeline)
                print("\n")
                
        def load_program(self, program):
            for i, instruction in enumerate(program):
                self.memory[i] = instruction
                

                
        def load_cacheL1(self, program):
            for i, instruction in enumerate(program):
                index = i % 8
                self.cache["L1"][index] = instruction
                self.cache_access += 1
                self.cache_miss += 1
                self.cache_miss_rate = self.cache_miss / self.cache_access
                print("Cache Miss Rate: ", self.cache_miss_rate)
                print("Cache Access Rate: ", self.cache_access_rate)
                print("Cache Miss: ", self.cache_miss)
                print("Cache Access: ", self.cache_access)
                print("Cache: ", self.cache)
                print("\n")
                
                
        def load_cacheL2(self, program):
            for i, instruction in enumerate(program):
                index = i % 8
                self.cache["L2"][index] = instruction
                self.cache_access += 1
                self.cache_miss += 1
                self.cache_miss_rate = self.cache_miss / self.cache_access
                print("Cache Miss Rate: ", self.cache_miss_rate)
                print("Cache Access Rate: ", self.cache_access_rate)
                print("Cache Miss: ", self.cache_miss)
                print("Cache Access: ", self.cache_access)
                print("Cache: ", self.cache)
                print("\n")
               
            
                

              
              


        simulator1 = CPU_SIMULATOR()
        simulator1.load_program("data_input.txt")
        simulator1.load_cache("data_input.txt")
        simulator1.run()
        
                

                

                    
                

        
        
