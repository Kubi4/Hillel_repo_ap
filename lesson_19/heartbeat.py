from datetime import datetime

key = "Key TSTFEED0300|7E3E|0400"
input_file = "hblog.txt"
output_file = "hb_test.log"

def extract_timestamp(line):
    pos = line.find("Timestamp ")
    if pos == -1:
        return None
    return line[pos + 10: pos + 18]

def analyze_heartbeat():
    timestamps = []
    with open(input_file, "r") as file:
        for line in file:
            if key in line:
                ts = extract_timestamp(line)
                if ts:
                    timestamps.append(ts)

    new_timestamps = []

    for time in timestamps:
        converted_time = datetime.strptime(time, "%H:%M:%S")
        new_timestamps.append(converted_time)

    timestamps = new_timestamps

    with open(output_file, "w") as log_file:
        for i in range(len(timestamps) - 1):
            current_time = timestamps[i]
            next_time = timestamps[i + 1]
            diff = abs((current_time - next_time).total_seconds())
            if 31 < diff < 33:
                log_file.write(
                    f"WARNING: Heartbeat {diff} sec at {next_time.time()}\n"
                )
            elif diff >= 33:
                log_file.write(
                    f"ERROR: Heartbeat {diff} sec at {next_time.time()}\n"
                )

if __name__ == "__main__":
    analyze_heartbeat()