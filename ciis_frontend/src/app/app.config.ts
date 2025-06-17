// ciis_frontend/src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { initializeApp, provideFirebaseApp } from '@angular/fire/app';
import { getAuth, provideAuth } from '@angular/fire/auth';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { authInterceptor } from './services/auth.interceptor';

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
    // Registra el interceptor
    provideHttpClient(withInterceptors([authInterceptor])),
    // Configuración de Firebase
    provideFirebaseApp(() => initializeApp(firebaseConfig)),
    provideAuth(() => getAuth()),
  ],
};
