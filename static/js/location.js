/**
 * Location Sharing Utility Functions
 * Provides common location-related functionality
 */

// Location utilities namespace
const LocationUtils = {
    /**
     * Check if geolocation is available in the browser
     * @returns {boolean}
     */
    isGeolocationAvailable: function() {
        return 'geolocation' in navigator;
    },

    /**
     * Get user-friendly error message for geolocation errors
     * @param {GeolocationPositionError} error 
     * @returns {string}
     */
    getErrorMessage: function(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                return 'Please allow location access in your browser settings.';
            case error.POSITION_UNAVAILABLE:
                return 'Location information is unavailable. Please check your GPS.';
            case error.TIMEOUT:
                return 'Location request timed out. Please try again.';
            default:
                return 'An unknown error occurred getting your location.';
        }
    },

    /**
     * Calculate distance between two points in meters
     * @param {number} lat1 
     * @param {number} lon1 
     * @param {number} lat2 
     * @param {number} lon2 
     * @returns {number} Distance in meters
     */
    calculateDistance: function(lat1, lon1, lat2, lon2) {
        const R = 6371e3; // Earth's radius in meters
        const φ1 = lat1 * Math.PI / 180;
        const φ2 = lat2 * Math.PI / 180;
        const Δφ = (lat2 - lat1) * Math.PI / 180;
        const Δλ = (lon2 - lon1) * Math.PI / 180;

        const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
                  Math.cos(φ1) * Math.cos(φ2) *
                  Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        return R * c;
    },

    /**
     * Format distance for display
     * @param {number} meters 
     * @returns {string}
     */
    formatDistance: function(meters) {
        if (meters < 1000) {
            return Math.round(meters) + ' m';
        }
        return (meters / 1000).toFixed(1) + ' km';
    },

    /**
     * Default geolocation options
     */
    defaultOptions: {
        enableHighAccuracy: true,
        timeout: 15000,
        maximumAge: 0
    },

    /**
     * Watch options (less strict for continuous updates)
     */
    watchOptions: {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 5000
    }
};

// Make it globally available
window.LocationUtils = LocationUtils;
