/**
 * Shared map tile layers and style switching for Bukamalu.
 * Used by share, host, and home (selection) map pages.
 */
const BukamaluMap = (function() {
    'use strict';

    /**
     * Create default and satellite tile layers.
     * @param {string} mapboxToken - Mapbox public access token (pk.*). If empty, uses OSM + Esri.
     * @returns {{ defaultLayer: L.TileLayer, satelliteLayer: L.TileLayer }}
     */
    function createTileLayers(mapboxToken) {
        var defaultLayer, satelliteLayer;
        if (mapboxToken) {
            defaultLayer = L.tileLayer(
                'https://api.mapbox.com/styles/v1/mapbox/streets-v12/tiles/256/{z}/{x}/{y}@2x?access_token=' + mapboxToken,
                { attribution: '© Mapbox © OpenStreetMap', maxZoom: 22 }
            );
            satelliteLayer = L.tileLayer(
                'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v12/tiles/256/{z}/{x}/{y}@2x?access_token=' + mapboxToken,
                { attribution: '© Mapbox © Maxar', maxZoom: 22 }
            );
        } else {
            defaultLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors',
                maxZoom: 19
            });
            satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
                attribution: '© Esri',
                maxZoom: 19
            });
        }
        return { defaultLayer: defaultLayer, satelliteLayer: satelliteLayer };
    }

    /**
     * Switch map between default and satellite base layer.
     * @param {L.Map} map - Leaflet map instance
     * @param {L.TileLayer} defaultLayer
     * @param {L.TileLayer} satelliteLayer
     * @param {string} style - 'default' or 'satellite'
     */
    function switchStyle(map, defaultLayer, satelliteLayer, style) {
        if (!map || !defaultLayer || !satelliteLayer) return;
        if (style === 'satellite') {
            map.removeLayer(defaultLayer);
            map.addLayer(satelliteLayer);
        } else {
            map.removeLayer(satelliteLayer);
            map.addLayer(defaultLayer);
        }
    }

    /**
     * Update active state of map style toggle buttons.
     * @param {string} style - 'default' or 'satellite'
     * @param {string} [selector] - CSS selector for buttons (default '.map-style-btn')
     */
    function updateStyleButtons(style, selector) {
        var sel = selector || '.map-style-btn';
        document.querySelectorAll(sel).forEach(function(btn) {
            btn.classList.toggle('active', btn.dataset.style === style);
        });
    }

    return {
        createTileLayers: createTileLayers,
        switchStyle: switchStyle,
        updateStyleButtons: updateStyleButtons
    };
})();
