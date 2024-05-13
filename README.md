# Shutdown Timer (Windows)

This project implements a simple Windows Shutdown Timer using Tkinter.

## Usage

1. Select the desired shutdown time from the dropdown menu.
2. Click on the "Shutdown" button to initiate the shutdown process.
3. To cancel the shutdown, click on the "Cancel Shutdown" button.

## Implementation Details

The project consists of the following components:

- **shutdown_time_label**: Label indicating the time until shutdown.
  
- **shutdown_time_dropdown**: Dropdown menu to select the shutdown time.
  
- **cancel_button**: Button to cancel the shutdown process.
  
- **remaining_time_label**: Label displaying the remaining time until shutdown.
  
- **remaining_time_display**: Label dynamically showing the remaining time in hours, minutes, and seconds.
  
- **start_button**: Button to initiate the shutdown process.
  
- **initiate_shutdown()**: Method to start the shutdown process based on the selected time.
  
- **cancel_shutdown()**: Method to cancel the shutdown process.
  
- **update_remaining_time()**: Method to update the remaining time display every second.

## Notes

- The shutdown time can be selected from predefined options ranging from 0.5 to 4 hours.
- The shutdown process is initiated using the `os.popen()` function with the `shutdown` command.
- The remaining time is updated dynamically using the `after()` method to recursively call the `update_remaining_time()` method every second.

## Dependencies

- **Tkinter**: Tkinter is used for creating the graphical user interface.
  
- **os**: The `os` module is used to interact with the operating system for initiating the shutdown process.

## Instructions

1. Install Python if not already installed.
2. Run the Python script.
3. Select the desired shutdown time and click on the "Shutdown" button to initiate the shutdown process.
4. To cancel the shutdown, click on the "Cancel Shutdown" button.
```