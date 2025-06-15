// Ubicación: src/app/app.config.ts
import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

// 1. Importa las herramientas de Firebase
import { initializeApp, provideFirebaseApp } from '@angular/fire/app';
import { getAuth, provideAuth } from '@angular/fire/auth';

// 2. Pega aquí la configuración que te dio Firebase
const firebaseConfig = {
  apiKey: "AIzaSyAdiLkKAEHej2nrwARQKyNnOwggPPg1I04",
  authDomain: "creaptica-ciis.firebaseapp.com",
  projectId: "creaptica-ciis",
  storageBucket: "creaptica-ciis.firebasestorage.app",
  messagingSenderId: "529742461581",
  appId: "1:529742461581:web:2e29305a1efe87634240c4",
  measurementId: "G-SM9C9QYCCD"
};

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideFirebaseApp(() => initializeApp(firebaseConfig)),
    provideAuth(() => getAuth())
  ]
};
