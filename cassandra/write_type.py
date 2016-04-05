
class WriteType(object):
    """
    For usage with :class:`.RetryPolicy`, this describe a type
    of write operation.
    """

    SIMPLE = 0
    """
    A write to a single partition key. Such writes are guaranteed to be atomic
    and isolated.
    """

    BATCH = 1
    """
    A write to multiple partition keys that used the distributed batch log to
    ensure atomicity.
    """

    UNLOGGED_BATCH = 2
    """
    A write to multiple partition keys that did not use the distributed batch
    log. Atomicity for such writes is not guaranteed.
    """

    COUNTER = 3
    """
    A counter write (for one or multiple partition keys). Such writes should
    not be replayed in order to avoid overcount.
    """

    BATCH_LOG = 4
    """
    The initial write to the distributed batch log that Cassandra performs
    internally before a BATCH write.
    """

    CAS = 5
    """
    A lighweight-transaction write, such as "DELETE ... IF EXISTS".
    """

WriteType.name_to_value = {
    'SIMPLE': WriteType.SIMPLE,
    'BATCH': WriteType.BATCH,
    'UNLOGGED_BATCH': WriteType.UNLOGGED_BATCH,
    'COUNTER': WriteType.COUNTER,
    'BATCH_LOG': WriteType.BATCH_LOG,
    'CAS': WriteType.CAS
}

