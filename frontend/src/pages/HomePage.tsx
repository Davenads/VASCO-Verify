import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Telescope, Database, CheckCircle2, BarChart3, Activity } from 'lucide-react'
import apiClient from '../services/api'

function HomePage() {
  const [health, setHealth] = useState<any>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const checkBackend = async () => {
      try {
        const healthData = await apiClient.checkHealth()
        setHealth(healthData)
      } catch (error) {
        console.error('Failed to connect to backend:', error)
      } finally {
        setLoading(false)
      }
    }

    checkBackend()
  }, [])

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-gray-900">
      {/* Header */}
      <header className="border-b border-gray-700 bg-gray-900/50 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <Telescope className="h-8 w-8 text-primary-400" />
              <h1 className="text-2xl font-bold text-white">Transient Analysis Platform</h1>
            </div>
            <div className="flex items-center space-x-2">
              {loading ? (
                <Activity className="h-5 w-5 text-yellow-400 animate-pulse" />
              ) : health ? (
                <div className="flex items-center space-x-2 text-green-400">
                  <div className="h-2 w-2 bg-green-400 rounded-full animate-pulse" />
                  <span className="text-sm">Backend Connected</span>
                </div>
              ) : (
                <div className="flex items-center space-x-2 text-red-400">
                  <div className="h-2 w-2 bg-red-400 rounded-full" />
                  <span className="text-sm">Backend Offline</span>
                </div>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="text-center mb-16">
          <h2 className="text-5xl font-bold text-white mb-4">
            Verify Historical Astronomical Transients
          </h2>
          <p className="text-xl text-gray-300 max-w-3xl mx-auto">
            AI-powered platform for analyzing POSS-I sky survey images (1949-1957) to detect
            and verify transient phenomena with scientific rigor.
          </p>
          {health && (
            <div className="mt-4 text-sm text-gray-400">
              v{health.version} • {health.environment}
            </div>
          )}
        </div>

        {/* Feature Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
          <Link to="/plates" className="group">
            <div className="card bg-gray-800/50 border-gray-700 hover:border-primary-500 transition-all duration-200 hover:shadow-lg hover:shadow-primary-500/20">
              <Database className="h-12 w-12 text-primary-400 mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-semibold text-white mb-2">FITS Plates</h3>
              <p className="text-gray-400 text-sm">
                Upload and manage historical sky survey images from POSS-I
              </p>
            </div>
          </Link>

          <Link to="/detection" className="group">
            <div className="card bg-gray-800/50 border-gray-700 hover:border-primary-500 transition-all duration-200 hover:shadow-lg hover:shadow-primary-500/20">
              <Telescope className="h-12 w-12 text-primary-400 mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-semibold text-white mb-2">AI Detection</h3>
              <p className="text-gray-400 text-sm">
                Run YOLOv8-based transient detection on uploaded plates
              </p>
            </div>
          </Link>

          <Link to="/verification" className="group">
            <div className="card bg-gray-800/50 border-gray-700 hover:border-primary-500 transition-all duration-200 hover:shadow-lg hover:shadow-primary-500/20">
              <CheckCircle2 className="h-12 w-12 text-primary-400 mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-semibold text-white mb-2">Verification</h3>
              <p className="text-gray-400 text-sm">
                Manually review and verify AI detections with catalog cross-matching
              </p>
            </div>
          </Link>

          <Link to="/analysis" className="group">
            <div className="card bg-gray-800/50 border-gray-700 hover:border-primary-500 transition-all duration-200 hover:shadow-lg hover:shadow-primary-500/20">
              <BarChart3 className="h-12 w-12 text-primary-400 mb-4 group-hover:scale-110 transition-transform" />
              <h3 className="text-xl font-semibold text-white mb-2">Analysis</h3>
              <p className="text-gray-400 text-sm">
                Statistical analysis and correlation with nuclear tests and UAP reports
              </p>
            </div>
          </Link>
        </div>

        {/* About Section */}
        <div className="card bg-gray-800/50 border-gray-700">
          <h3 className="text-2xl font-semibold text-white mb-4">About This Platform</h3>
          <div className="prose prose-invert max-w-none">
            <p className="text-gray-300 mb-4">
              This platform enables independent verification of groundbreaking research published in
              <em className="text-primary-400"> Nature Scientific Reports</em> linking astronomical
              transients with nuclear weapons testing and UAP reports during 1949-1957.
            </p>
            <p className="text-gray-300">
              Using AI-powered detection (YOLOv8) combined with manual verification, researchers
              and enthusiasts can reproduce published findings and contribute to this fascinating
              area of astronomical research.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default HomePage
