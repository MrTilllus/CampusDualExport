# CampusDualExport

> the following quick and dirty script is provided "as-is" with no support, further development or security affirmations.
> Only use it if you know what it does.

## How to use:
1. login to CampusDual
2. view calendar
3. press F12 to show developer console
4. switch to "Network"
5. find your calendar-json request url
![](https://github.com/VinzSpring/CampusDualExport/blob/master/howto.jpg)
6. write a python script to export data into calendar app readable .csv

```
if __name__ == '__main__':
    export_to_csv("./test.csv", "https://selfservice.campus-dual.de/room/json?userid=[YOUR_USER_ID]&hash=[MAGIC_HASH]&start=[TIME_STAMP_START]&end=[TIME_STAMP_END]")
```
