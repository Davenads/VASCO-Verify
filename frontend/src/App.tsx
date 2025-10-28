import { Routes, Route } from 'react-router-dom'
import HomePage from './pages/HomePageSimple'
import PlatesPage from './pages/PlatesPage'
import DetectionPage from './pages/DetectionPage'
import VerificationPage from './pages/VerificationPage'
import AnalysisPage from './pages/AnalysisPage'
import TestPage from './pages/TestPage'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Routes>
        <Route path="/test" element={<TestPage />} />
        <Route path="/" element={<HomePage />} />
        <Route path="/plates" element={<PlatesPage />} />
        <Route path="/detection" element={<DetectionPage />} />
        <Route path="/verification" element={<VerificationPage />} />
        <Route path="/analysis" element={<AnalysisPage />} />
      </Routes>
    </div>
  )
}

export default App
