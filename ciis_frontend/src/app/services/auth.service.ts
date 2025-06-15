// Ubicación: src/app/services/auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject, tap } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://127.0.0.1:8000/ciis/api/auth/login/';
  private readonly TOKEN_KEY = 'auth_token';

  private authStatus = new BehaviorSubject<boolean>(this.hasToken());
  public isAuthenticated = this.authStatus.asObservable();

  constructor(private http: HttpClient, private router: Router) { }

  private hasToken(): boolean {
    return !!localStorage.getItem(this.TOKEN_KEY);
  }

  login(credentials: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, credentials).pipe(
      tap(response => {
        // --- CORRECCIÓN AQUÍ ---
        // El token viene en la propiedad 'access', no 'access_token'.
        if (response && response.key) {
          localStorage.setItem(this.TOKEN_KEY, response.access);
          this.authStatus.next(true);
        }
      })
    );
  }

  logout(): void {
    localStorage.removeItem(this.TOKEN_KEY);
    this.authStatus.next(false);
    this.router.navigate(['/login']);
  }

  getToken(): string | null {
    return localStorage.getItem(this.TOKEN_KEY);
  }

  isLoggedIn(): boolean {
    return this.authStatus.getValue();
  }
}
