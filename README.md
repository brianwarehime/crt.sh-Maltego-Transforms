# crt.sh Maltego Transforms
Maltego Local Transforms for crt.sh

## Requirements
- You need to have `requests` and `BeautifulSoup` installed. Which can be done through `pip install requests` and `pip install beautifulsoup`

## Installation
- Grab the .mtz file I have hosted on my github, here.
- Import this .mtz file into Maltego, by going to the top-left icon, then Import, then Import Configuration.
- Grab the Python code from my Github for the transforms. You'll grab crtsh.py and MaltegoTransform.py from this repo.
- Move the crtsh folder to `/opt/Maltego` *You'll most likely need to create this folder first

## Using this Transform
Once you import the transform, you'll add a new Website entity to the graph, and enter the domain as the entity name (i.e. nullsecure.org). The transform will search for any other hosts that have certificates under your domain name (i.e. test.nullsecure.org, stuff.nullsecure.org, etc.)

## Sample Results

![https://i.imgur.com/0Ga8gsS.png](https://i.imgur.com/0Ga8gsS.png)

That should be all you need to get going, if you run into any issues or have bug reports/issues, please shoot them to me at brian@nullsecure.org, or on twitter @brian_warehime, or file an issue in Github.

Thanks!
