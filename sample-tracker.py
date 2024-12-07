import json
import os
import csv

# File to store sample data

JSON_DATA_FILE = 'data.json'

# Load samples from the JSON file
def load_samples():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Save samples to the JSON file
def save_samples(samples):
    with open(DATA_FILE, 'w') as file:
        json.dump(samples, file, indent=4)

# Add a new sample
def add_sample(samples):
    sample_id = input("Enter Sample ID: ")
    sample_type = input("Enter Sample Type: ")
    location = input("Enter Storage Location: ")
    status = input("Enter Status: ")
    
    sample = {
        "sample_id": sample_id,
        "sample_type": sample_type,
        "location": location,
        "status": status
    }
    samples.append(sample)
    save_samples(samples)
    print("Sample added successfully!")

# View all samples
def view_samples(samples):
    if not samples:
        print("No samples found.")
        return
    for idx, sample in enumerate(samples):
        print(f"{idx + 1}. ID: {sample['sample_id']}, Type: {sample['sample_type']}, Location: {sample['location']}, Status: {sample['status']}")

# Update a sample
def update_sample(samples):
    view_samples(samples)
    index = int(input("Enter the number of the sample to update: ")) - 1
    if 0 <= index < len(samples):
        sample = samples[index]
        sample['sample_type'] = input(f"Enter new Sample Type (current: {sample['sample_type']}): ") or sample['sample_type']
        sample['location'] = input(f"Enter new Storage Location (current: {sample['location']}): ") or sample['location']
        sample['status'] = input(f"Enter new Status (current: {sample['status']}): ") or sample['status']
        save_samples(samples)
        print("Sample updated successfully!")
    else:
        print("Invalid sample number.")

# Delete a sample
def delete_sample(samples):
    view_samples(samples)
    index = int(input("Enter the number of the sample to delete: ")) - 1
    if 0 <= index < len(samples):
        samples.pop(index)
        save_samples(samples)
        print("Sample deleted successfully!")
    else:
        print("Invalid sample number.")

# Export samples to a CSV file
def export_samples_to_csv(samples):
    csv_file = 'samples.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["sample_id", "sample_type", "location", "status"])
        writer.writeheader()
        writer.writerows(samples)
    print(f"Samples exported successfully to {csv_file}!")

# Main function to run the application
def main():
    samples = load_samples()
    while True:
        print("\nSample Tracker")
        print("1. Add Sample")
        print("2. View Samples")
        print("3. Update Sample")
        print("4. Delete Sample")
        print("5. Export Samples to CSV")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_sample(samples)
        elif choice == '2':
            view_samples(samples)
        elif choice == '3':
            update_sample(samples)
        elif choice == '4':
            delete_sample(samples)
        elif choice == '5':
            export_samples_to_csv(samples)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
