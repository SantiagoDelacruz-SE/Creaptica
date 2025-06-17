// ciis_frontend/src/app/app.component.ts
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';
import { AuthService } from './services/auth.service';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'ciis_frontend';
  // CORREGIDO: Declaramos la propiedad primero
  userProfile$: Observable<any>;

  constructor(public authService: AuthService) {
    // CORREGIDO: La inicializamos dentro del constructor
    this.userProfile$ = this.authService.userProfile$;
  }

  logout(): void {
    this.authService.logout();
  }
}
