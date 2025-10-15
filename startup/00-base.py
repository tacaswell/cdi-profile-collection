import nslsii
import os

from tiled.client import from_profile, from_uri
from bluesky.callbacks.tiled_writer import TiledWriter
from ophyd.sim import det1, det2
from bluesky.plans import count

nslsii.configure_base(
    get_ipython().user_ns,
    publish_documents_with_kafka=False,
)

tiled_writing_client = from_uri(
    "https://tiled-staging.nsls2.bnl.gov/api/v1/metadata/cdi/raw",
    api_key=os.environ["TILED_BLUESKY_WRITING_API_KEY_CDI"],
)

c = tiled_reading_client = from_uri(
    "https://tiled-staging.nsls2.bnl.gov/api/v1/metadata/cdi/raw",
    include_data_sources=True,
)

RE.md["tiled_access_tags"] = ["cdi_beamline"]

tw = TiledWriter(client=tiled_writing_client)

RE.subscribe(tw)
