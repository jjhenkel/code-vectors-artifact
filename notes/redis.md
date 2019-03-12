# Redis Specs

## `clusterNodeAddSlave`

Anywhere there is a call to clusterNodeAddSlave is also 
a place that `x->slaveof` gets set.

```
!->slaveof_$p1_clusterNodeAddSlave
clusterNodeAddSlave
```

## `replicationSetMaster`

Interesting behavior: this requires good parametric support so I'm
not sure if we can capture it.

```
nodeIsSlave(x)_$NEQ_0
x->slaveof_$NEQ_0
replicationSetMaster(x->slaveof->ip, x->slaveof->port)
```

## `clusterNodeRemoveSlave`

```
nodeIsMaster(x)_$EQ_0 or nodeIsSlave(x)_$NEQ_0
clusterNodeRemoveSlave_$po_$NEQ_0
clusterNodeRemoveSlave(x->slaveof, x)
```

## `createClusterNode`

Sometimes prefixed with: `clusterLookupNode clusterLookupNode_$EQ_0`.

```
createClusterNode
createClusterNode_$PARAMTO_clusterAddNode
clusterAddNode

```