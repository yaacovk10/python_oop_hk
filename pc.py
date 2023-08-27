class PC:
    def __init__(self, ram_memory, storage_capacity, cpu):
        self.ram_memory = ram_memory
        self.storage_capacity = storage_capacity
        self.cpu = cpu
        self.is_on = False
        self.used_storage = 0

    def turn_on(self):
        self.is_on = True
        return "PC is now ON."

    def turn_off(self):
        self.is_on = False
        return "PC is now OFF."

    def cpu_consumption(self, usage_percentage):
        if self.is_on:
            return f"CPU consumption: {usage_percentage}%"
        else:
            return "PC is turned off."

    def ram_consumption(self, used_memory):
        if self.is_on:
            return f"RAM consumption: {used_memory} GB"
        else:
            return "PC is turned off."

    def file_operation(self, operation, file_size):
        if self.is_on:
            if operation == "create":
                self.used_storage += file_size
                return f"File created. Storage used: {self.used_storage} GB"
            elif operation == "delete":
                self.used_storage -= file_size
                return f"File deleted. Storage used: {self.used_storage} GB"
            else:
                return "Invalid operation."
        else:
            return "PC is turned off."

    def network_connectivity(self):
        if self.is_on:
            return "Connected to the network."
        else:
            return "PC is turned off."

# Test the updated PC class
if __name__ == "__main__":
    my_pc = PC(16, 1000, "Intel i7")
    print(f"RAM: {my_pc.ram_memory} GB, Storage: {my_pc.storage_capacity} GB, CPU: {my_pc.cpu}")
    
    print(my_pc.turn_on())
    print(my_pc.network_connectivity())
    print(my_pc.file_operation("create", 5))
    print(my_pc.file_operation("delete", 2))
    print(my_pc.file_operation("invalid", 1))
    
    print(my_pc.turn_off())
    print(my_pc.network_connectivity())
    print(my_pc.file_operation("create", 3))
