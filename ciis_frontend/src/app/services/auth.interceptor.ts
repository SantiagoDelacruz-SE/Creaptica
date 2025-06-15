// ciis_frontend/src/app/services/auth.interceptor.ts
import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthService } from './auth.service';
import { switchMap, take } from 'rxjs/operators';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authService = inject(AuthService);
  const djangoApiUrl = 'http://127.0.0.1:8000/api/'; // URL base de tu API

  // Solo intercepta las peticiones a tu API de Django
  if (!req.url.startsWith(djangoApiUrl)) {
    return next(req);
  }

  return authService.idToken$.pipe(
    take(1), // Toma el valor actual del token y se desuscribe
    switchMap(token => {
      if (token) {
        const clonedReq = req.clone({
          headers: req.headers.set('Authorization', `Bearer ${token}`),
        });
        return next(clonedReq);
      }
      // Si no hay token, envía la petición sin modificar
      return next(req);
    })
  );
};
