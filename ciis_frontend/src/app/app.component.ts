// Ubicación: src/app/app.component.ts
import { Component, OnInit } from '@angular/core'; // Añade OnInit
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { AuthService } from './services/auth.service'; // 1. Importa el servicio
import { Observable } from 'rxjs'; // 2. Importa Observable

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'] // Asegúrate que la extensión es .scss si usas SASS
})
export class AppComponent implements OnInit {
  title = 'ciis_frontend';

  // 3. Propiedad para guardar el estado de autenticación como un Observable
  isLoggedIn$!: Observable<boolean>;

  // 4. Inyecta el AuthService
  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    // 5. Asigna el observable del servicio a nuestra propiedad local
    this.isLoggedIn$ = this.authService.isAuthenticated;
  }

  // 6. Método para manejar el logout desde el template
  onLogout(): void {
    this.authService.logout();
  }
}
