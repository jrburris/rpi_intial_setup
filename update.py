import apt

cache = apt.Cache()
cache.update()
cache.open(None)
cache.upgrade()
for pkg in cache.getChanges():
    print pkg.sourcePackageName, pkg.isUpgradeable
