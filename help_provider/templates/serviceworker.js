const CACHE_NAME = 'help-provider-v1';
const assets = [
    '/help_provider/',
    '/static/css/style.css',
    '/static/images/icon-192.png'
];

// Install service worker
self.addEventListener('install', evt => {
    evt.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            cache.addAll(assets);
        })
    );
});

// Fetching content
self.addEventListener('fetch', evt => {
    evt.respondWith(
        caches.match(evt.request).then(cacheRes => {
            return cacheRes || fetch(evt.request);
        })
    );
});