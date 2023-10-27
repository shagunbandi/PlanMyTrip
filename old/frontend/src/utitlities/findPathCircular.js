function swapEdges(points, i, j) {
  const t = points[i]
  points[i] = points[j]
  points[j] = t
  return points
}

function calculateDistance(point1, point2, getX, getY) {
  const [x1, y1] = [getX(point1), getY(point1)]
  const [x2, y2] = [getX(point2), getY(point2)]
  return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
}

function findNearestNeighbor(currentPoint, unvisitedPoints, getX, getY) {
  let nearestNeighbor = unvisitedPoints[0]
  let shortestDistance = calculateDistance(currentPoint, nearestNeighbor, getX, getY)

  for (let i = 1; i < unvisitedPoints.length; i++) {
    const point = unvisitedPoints[i]
    const distance = calculateDistance(currentPoint, point, getX, getY)

    if (distance < shortestDistance) {
      shortestDistance = distance
      nearestNeighbor = point
    }
  }

  return nearestNeighbor
}

function calculatePath(points, getX, getY) {
  const startingPoint = points[0]
  const unvisitedPoints = points.slice(1)
  const path = [startingPoint]

  let currentPoint = startingPoint

  while (unvisitedPoints.length > 0) {
    const nearestNeighbor = findNearestNeighbor(currentPoint, unvisitedPoints, getX, getY)
    path.push(nearestNeighbor)

    const index = unvisitedPoints.indexOf(nearestNeighbor)
    unvisitedPoints.splice(index, 1)

    currentPoint = nearestNeighbor
  }

  return path
}

const find = (points, getX = (point) => point[0], getY = (point) => point[1], startIdx = 0) => {
  swapEdges(points, 0, startIdx)
  const path = calculatePath(points, getX, getY)
  console.log(path)
  return path
}

export default find
