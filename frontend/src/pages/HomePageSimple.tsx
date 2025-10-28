import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
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
    <div style={{ minHeight: '100vh', background: 'linear-gradient(to bottom right, #1a1a2e, #0f3460, #1a1a2e)', color: 'white' }}>
      {/* Header */}
      <header style={{ borderBottom: '1px solid #374151', padding: '1rem' }}>
        <div style={{ maxWidth: '1280px', margin: '0 auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1 style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>Transient Analysis Platform</h1>
          <div>
            {loading ? (
              <span>Checking backend...</span>
            ) : health ? (
              <span style={{ color: '#10b981' }}>✓ Backend Connected</span>
            ) : (
              <span style={{ color: '#ef4444' }}>✗ Backend Offline</span>
            )}
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '4rem 1rem' }}>
        <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
          <h2 style={{ fontSize: '3rem', fontWeight: 'bold', marginBottom: '1rem' }}>
            Verify Historical Astronomical Transients
          </h2>
          <p style={{ fontSize: '1.25rem', maxWidth: '800px', margin: '0 auto', opacity: 0.9 }}>
            AI-powered platform for analyzing POSS-I sky survey images (1949-1957) to detect
            and verify transient phenomena with scientific rigor.
          </p>
          {health && (
            <div style={{ marginTop: '1rem', fontSize: '0.875rem', opacity: 0.7 }}>
              v{health.version} • {health.environment}
            </div>
          )}
        </div>

        {/* Feature Cards */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '1.5rem',
          marginBottom: '3rem'
        }}>
          <Link to="/plates" style={{ textDecoration: 'none' }}>
            <div style={{
              background: 'rgba(31, 41, 55, 0.5)',
              border: '1px solid #374151',
              borderRadius: '0.5rem',
              padding: '1.5rem',
              transition: 'all 0.2s',
              cursor: 'pointer'
            }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '0.5rem' }}>📊 FITS Plates</h3>
              <p style={{ fontSize: '0.875rem', opacity: 0.8 }}>
                Upload and manage historical sky survey images from POSS-I
              </p>
            </div>
          </Link>

          <Link to="/detection" style={{ textDecoration: 'none' }}>
            <div style={{
              background: 'rgba(31, 41, 55, 0.5)',
              border: '1px solid #374151',
              borderRadius: '0.5rem',
              padding: '1.5rem',
              transition: 'all 0.2s',
              cursor: 'pointer'
            }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '0.5rem', color: 'white' }}>🔭 AI Detection</h3>
              <p style={{ fontSize: '0.875rem', opacity: 0.8, color: 'white' }}>
                Run YOLOv8-based transient detection on uploaded plates
              </p>
            </div>
          </Link>

          <Link to="/verification" style={{ textDecoration: 'none' }}>
            <div style={{
              background: 'rgba(31, 41, 55, 0.5)',
              border: '1px solid #374151',
              borderRadius: '0.5rem',
              padding: '1.5rem',
              transition: 'all 0.2s',
              cursor: 'pointer'
            }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '0.5rem', color: 'white' }}>✓ Verification</h3>
              <p style={{ fontSize: '0.875rem', opacity: 0.8, color: 'white' }}>
                Manually review and verify AI detections with catalog cross-matching
              </p>
            </div>
          </Link>

          <Link to="/analysis" style={{ textDecoration: 'none' }}>
            <div style={{
              background: 'rgba(31, 41, 55, 0.5)',
              border: '1px solid #374151',
              borderRadius: '0.5rem',
              padding: '1.5rem',
              transition: 'all 0.2s',
              cursor: 'pointer'
            }}>
              <h3 style={{ fontSize: '1.25rem', fontWeight: '600', marginBottom: '0.5rem', color: 'white' }}>📈 Analysis</h3>
              <p style={{ fontSize: '0.875rem', opacity: 0.8, color: 'white' }}>
                Statistical analysis and correlation with nuclear tests and UAP reports
              </p>
            </div>
          </Link>
        </div>

        {/* About Section */}
        <div style={{
          background: 'rgba(31, 41, 55, 0.5)',
          border: '1px solid #374151',
          borderRadius: '0.5rem',
          padding: '1.5rem'
        }}>
          <h3 style={{ fontSize: '1.5rem', fontWeight: '600', marginBottom: '1rem' }}>About This Platform</h3>
          <p style={{ marginBottom: '1rem', opacity: 0.9 }}>
            This platform enables independent verification of groundbreaking research published in
            <em style={{ color: '#60a5fa' }}> Nature Scientific Reports</em> linking astronomical
            transients with nuclear weapons testing and UAP reports during 1949-1957.
          </p>
          <p style={{ opacity: 0.9 }}>
            Using AI-powered detection (YOLOv8) combined with manual verification, researchers
            and enthusiasts can reproduce published findings and contribute to this fascinating
            area of astronomical research.
          </p>
        </div>
      </div>
    </div>
  )
}

export default HomePage
