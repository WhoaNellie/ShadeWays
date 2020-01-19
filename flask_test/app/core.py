import sys
sys.path.append("../../../ShadeWays")
import shadow_calc
from shadow_calc.shadowFinder import *
from shadow_calc.test_code_cleaned import *
from shadow_calc.osm_api import *
from shadow_calc.overlap import *

def core(tup_start, tup_end):
    path_coords, directions_result = googleapi(tup_start, tup_end)
    osm = OSMAPI(path_coords)
    osm.run_pointwise_query()
    important_values = osm.get_elements()
    lat0, long0 = important_values[0][0:2]
    shadowlist = shadowFinder(important_values, lat0, long0)
    percent = overlap(shadowlist,path_coords)
    return percent, directions_result

print(core((34,-118),(35,-115))[0])