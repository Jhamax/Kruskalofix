import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';
import { FBXLoader } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/FBXLoader.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x222222);

const camera = new THREE.PerspectiveCamera(45, window.innerWidth/window.innerHeight, 0.1, 1000);
camera.position.set(0, 1.6, 3);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Kontrol kamera
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(0, 1, 0);
controls.update();

// Lampu
const dirLight = new THREE.DirectionalLight(0xffffff, 1);
dirLight.position.set(0, 10, 10);
scene.add(dirLight);

const ambLight = new THREE.AmbientLight(0x404040, 2);
scene.add(ambLight);

const loader = new FBXLoader();
loader.load(
  'avatar.fbx',
  (object) => {
    console.log('Model loaded:', object);
    object.scale.set(0.01, 0.01, 0.01);
    object.position.set(0, 0, 0);
    scene.add(object);
  },
  (xhr) => {
    console.log(`Loading model: ${(xhr.loaded / xhr.total * 100).toFixed(2)}%`);
  },
  (error) => {
    console.error('Error loading model:', error);
  }
);

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}

window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth/window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});

animate();
