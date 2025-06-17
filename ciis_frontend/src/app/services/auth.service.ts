// ciis_frontend/src/app/services/auth.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Auth, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut, onAuthStateChanged, User, AuthCredential } from '@angular/fire/auth';
import { BehaviorSubject, from, Observable, of } from 'rxjs';
import { switchMap, shareReplay } from 'rxjs/operators';
import { Router } from '@angular/router';

// Define el tipo para las credenciales de login/registro
interface Credentials {
  email: string;
  password: string;
}

// Define el tipo para el perfil del usuario que viene de Django
interface UserProfile {
  id: number;
  username: string;
  email: string;
  perfil_ciis: {
    rol: 'ADMIN_CIIS' | 'INVESTIGADOR' | 'DOCENTE' | 'ESTUDIANTE' | null;
  };
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private djangoApiUrl = 'http://127.0.0.1:8000/api';

  public user$ = new BehaviorSubject<User | null>(null);
  public idToken$ = new BehaviorSubject<string | null>(null);
  public userProfile$: Observable<UserProfile | null>;

  constructor(
    private fireAuth: Auth,
    private router: Router,
    private http: HttpClient
  ) {
    onAuthStateChanged(this.fireAuth, (user) => {
      this.user$.next(user);
      if (user) {
        from(user.getIdToken()).subscribe(token => this.idToken$.next(token));
      } else {
        this.idToken$.next(null);
      }
    });

    this.userProfile$ = this.user$.pipe(
      switchMap(user => {
        if (user) {
          return this.http.get<UserProfile>(`${this.djangoApiUrl}/profile/`);
        }
        return of(null);
      }),
      shareReplay(1)
    );
  }

  // CORREGIDO: Se añadieron tipos a las credenciales
  login({ email, password }: Credentials): Observable<any> {
    return from(signInWithEmailAndPassword(this.fireAuth, email, password));
  }

  // CORREGIDO: Se añadieron tipos a las credenciales
  register({ email, password }: Credentials): Observable<any> {
    return from(createUserWithEmailAndPassword(this.fireAuth, email, password));
  }

  logout() {
    signOut(this.fireAuth).then(() => {
      this.router.navigate(['/login']);
    });
  }
}
