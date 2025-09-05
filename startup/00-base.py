import nslsii

nslsii.configure_base(
    get_ipython().user_ns,
    broker_name="temp",
    publish_documents_with_kafka=False,
    redis_url="info.cdi.nsls2.bnl.gov",
)
