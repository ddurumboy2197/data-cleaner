import time
import psutil
import os

class PerformanceBenchmarkTool:
    def __init__(self):
        self.process = psutil.Process(os.getpid())

    def get_cpu_usage(self):
        return self.process.cpu_percent(interval=1)

    def get_memory_usage(self):
        return self.process.memory_percent()

    def get_disk_usage(self):
        return psutil.disk_usage('/').percent

    def get_network_usage(self):
        return psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    def benchmark(self):
        print("Boshlang'ich holat:")
        print(f"CPU ishlatilishi: {self.get_cpu_usage()}%")
        print(f"Xotira ishlatilishi: {self.get_memory_usage()}%")
        print(f"Disq ishlatilishi: {self.get_disk_usage()}%")
        print(f"Network ishlatilishi: {self.get_network_usage()} bytes")

        start_time = time.time()
        for i in range(10000000):
            pass
        end_time = time.time()

        print("\nIshlatilgan holat:")
        print(f"CPU ishlatilishi: {self.get_cpu_usage()}%")
        print(f"Xotira ishlatilishi: {self.get_memory_usage()}%")
        print(f"Disq ishlatilishi: {self.get_disk_usage()}%")
        print(f"Network ishlatilishi: {self.get_network_usage()} bytes")

        print(f"Ishlatilgan vaqtdan: {end_time - start_time} soniya")

if __name__ == "__main__":
    tool = PerformanceBenchmarkTool()
    tool.benchmark()
```

Kodda quyidagi funksiyalar mavjud:

- `get_cpu_usage()`: CPU ishlatilishini %da qaytaradi.
- `get_memory_usage()`: Xotira ishlatilishini %da qaytaradi.
- `get_disk_usage()`: Disq ishlatilishini %da qaytaradi.
- `get_network_usage()`: Network ishlatilishini bytesda qaytaradi.
- `benchmark()`: Boshlang'ich holatni chiqarib, 10 million marta `for` tsiklini bajarib, keyin ishlatilgan holatni chiqarib, ishlatilgan vaqtdan xabarni chiqaradi.
