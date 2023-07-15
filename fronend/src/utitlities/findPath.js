function calculateDistance(points, i, j, getX, getY) {
  const [x1, y1] = [getX(points[i]), getY(points[i])]
  const [x2, y2] = [getX(points[j]), getY(points[j])]
  return Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
}

function calculateTotalDistance(points, getX, getY) {
  let totalDistance = 0
  for (let i = 0; i < points.length - 1; i++) {
    totalDistance += calculateDistance(points, i, i + 1, getX, getY)
  }
  return totalDistance
}

function swapEdges(points, i, k) {
  const newPoints = [...points]
  newPoints[i] = points[k]
  newPoints[k] = points[i]
  return newPoints
}

function twoOptTSP(points, getX, getY) {
  const n = points.length
  let bestDistance = Infinity
  let bestPath = points

  for (let i = 1; i < n - 2; i++) {
    for (let k = i; k < n - 1; k++) {
      const newPath = swapEdges(points, i, k)
      const newDistance = calculateTotalDistance(newPath, getX, getY)

      if (newDistance < bestDistance) {
        bestDistance = newDistance
        bestPath = newPath
      }
    }
  }

  return {
    path: bestPath,
    distance: bestDistance
  }
}

const calculatePath = (
  points,
  getX = (point) => point[0],
  getY = (point) => point[1],
  startIdx = 0,
  endIdx = points.length - 1
) => {
  if (startIdx != endIdx) {
    points = swapEdges(points, 0, startIdx)
    points = swapEdges(points, points.length - 1, endIdx)
    return twoOptTSP(points, getX, getY).path
  } else {
    points = swapEdges(points, 0, startIdx)
    points.push(points[0])
    return twoOptTSP(points, getX, getY).path
  }
}

export default calculatePath
