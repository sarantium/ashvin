Wardley Map PseudoCode Syntax

| Element       | Description                                   | Syntax Example                        | Notes                                                            |
| ------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------- |
| Title         | The title of the Wardley Map.                 | title Tea Shop                        | Only one title per map.                                          |
| Anchor        | Reference points on the map                   | anchor Business [0.95, 0.63]          | Position is given by y,x coordinates                             |
| Component     | A node or item on the map.                    | component Cup of Tea [0.80, 0.58]     | Position is given by y,x coordinates                             |
| Connection    | Dependency between components                 | Cup of Tea->Kettle                    | Arrow indicates direction of dependency. No connection prefix    |
| Inertia       | Resistance to change of a component           | component Cup [0.69, 0.62] inertia    | Optional for components. Position is given by y,x coordinates    |
| Evolve        | Movement of a component on the evolution axis | evolve Cup 0.9                        | Optional for components. Position is given by an x coordinate    |
| Buy           | Indicates a purchasing action.                | buy Cup                               | Use off the shelf products. Changes the component style          |
| Build         | Indicates a purchasing action.                | build Cup                             | Build in-house. Changes the component style                      |
| Outsource     | Indicates a purchasing action.                | outsource Cup                         | Outsource to utility suppliers. Changes the component style      |
| Pioneers      | Bounded box denoting a team type              | pioneers [0.90, 0.16, 0.68, 0.38]     | Position is given by y,x,y,x coordinates. Pioneers explore       |
| Settlers      | Bounded box denoting a team type              | settlers [0.90, 0.16, 0.68, 0.38]     | Position is given by y,x,y,x coordinates. Settlers scale         |
| Town Planners | Bounded box denoting a team type              | townplanners [0.90, 0.16, 0.68, 0.38] | Position is given by y,x,y,x coordinates. Planners industrialise |
| Market        | Component denoting a competitive marketplace  | market AppStore [0.32, 0.65]          | Position is given by y,x coordinates                             |

Special Instructions :

1. For 'Pioneers', 'Settlers', and 'Town Planners', the coordinates for the bounding box are in the order of [y1, x1, y2, x2], where 'y1' is the upper boundary on the y-axis and must be greater than 'y2', the lower boundary. Similarly, 'x1' is the left boundary on the x-axis and must be less than 'x2', the right boundary. These coordinates define the rectangle representing the area of operation for each team type on the map.
2. Connection elements should not have connection as a prefix. Only the -> link is needed.
