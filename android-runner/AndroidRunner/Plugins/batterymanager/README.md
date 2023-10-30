# BatteryManager Plugin
This plugin uses the Android BatteryManager API to gather battery related data. The plugin works using the 
[BatteryManager companion app](https://github.com/S2-group/batterymanager-companion/releases). 

## Dependencies and Requirements
* BatteryManager companion app has to be installed on the device with all permissions granted. 
  * [apk](https://github.com/S2-group/batterymanager-companion/releases) (https://github.com/S2-group/batterymanager-companion/releases)
  * [code](https://github.com/S2-group/batterymanager-companion/) (https://github.com/S2-group/batterymanager-companion/)
* `BATTERY_PLUGGED_DOCK` data point is available for Android version Tiramisu (API Level 33) and above.
* `EXTRA_BATTERY_LOW` data point is available for Android version P (Pie) (API Level 28) and above.
* The `EXTRA_*` values do not update between runs with the initial Android Runner version. In order to have the values 
  update as intended, the `device.unplug(restart)` line in [AndroidRunner/Experiment.py](../../Experiment.py), 
  `prepare_device` function should be removed.
## Configuration
The following is an example configuration that contains possible values for the `data_points` and 
`persistency strategy` fields.

```json
  ...
  "profilers": {
    "batterymanager": {
      "experiment_aggregation": "default",
      "sample_interval": 1000,
      "data_points": [
        "BATTERY_PROPERTY_CURRENT_NOW", "EXTRA_VOLTAGE"
      ],
      "persistency_strategy": [
        "adb_log"
      ]
    }
  },
  ...
```
**experiment_aggregation** *string*
Aggregates the results of each run of each app into one csv file (`Aggregated_Results_Batterymanager.csv`).
Column descriptions 
* `device` name of the device.
* `subject` name of the application.
* `run` run number of the application in the experiment.
* `UPPERCASE_COLUMN_NAMES` contain the average of the matching column name that was specified in the config for that 
  particular run.
* If the *config.json* contains both `BATTERY_PROPERTY_CURRENT_NOW` and `EXTRA_VOLTAGE` fields, then the following columns will
  also be created:
  * `Energy trapz (J)` energy consumption of the run computed with the trapezoid method.
  * `Energy simple (J)` energy consumption of the run computed simply by multiplying the average power by time.
  * `Avg power (W)` average power consumption of the run.

**sample_interval** *int* 
How often the data should be gathered in milliseconds. (can be equal to 0, in which case the companion app will record 
continuously, see Limitations and Known Issues section for more information on recording continuously).

**data_points** *Array<string>* 
The data points that should be gathered. All the available data points are listed above in the config sample.
For further information on each of the data points, please refer to the 
[Android BatteryManager API documentation](https://developer.android.com/reference/android/os/BatteryManager#summary)
(https://developer.android.com/reference/android/os/BatteryManager#summary).
* `BATTERY_PLUGGED_DOCK` data point is available for Android version Tiramisu (API Level 33) and above.
* `EXTRA_BATTERY_LOW` data point is available for Android version P (Pie) (API Level 28) and above.

**persistency_strategy** *Array<string>* 
The persistency strategy that should be used. The available options are:
* `adb_log` - uses the Android logs to extract the data from the companion app.
* `csv` - stores the data in a CSV file on the device, then pulls the file from the device and stores it on the computer.
  ***Flaky on old devices!! Fix needed in the companion app.***

## Limitations and Known Issues
* The companion app keeps everything in memory and then dumps it to a csv file. This means that if the user wants to use 
  memory as a dependent variable, they should not use the `csv` persistency strategy.
* Very low `sample_interval` values causes the number of observations from the companion app to be inconsistent between 
  runs. (i.e., one run might have 1000 rows, next run could have 800, or 1200 rows).
* Running the BatteryManager app, using the `csv` persistency strategy can crash on older devices. We recommend using 
  `adb_log` strategy.

