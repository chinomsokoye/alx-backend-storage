>>> cache = Cache()
>>> cache.store("foo")
>>> cache.store("bar")
>>> cache.store(42)
>>> replay(cache.store)
Cache.store was called 3 times:
Cache.store(*('foo',)) -> 13bdf-efg565-gchsjk-bvdff55654
Cache.store(*('bar',)) -> 11rgf-e56565-gchghk-bvdfgh654
Cache.store(*(42,)) -> 15bfgh-efert5-grtyjk-bvdtyhj654
