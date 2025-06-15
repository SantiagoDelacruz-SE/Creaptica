// Ubicación: src/app/components/auth/login/login.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../../services/auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
// --- ASEGÚRATE DE QUE LA PALABRA 'export' ESTÉ AQUÍ ---
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;
  loginError: string | null = null;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]]
    });
  }

  onSubmit(): void {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched();
      return;
    }

    this.loginError = null;

    this.authService.login(this.loginForm.value).subscribe({
      next: (response) => {
        console.log('Login exitoso!', response);
        this.router.navigate(['/inicio']);
      },
      error: (err) => {
        console.error('Error en el login:', err);
        if (err.error && err.error.non_field_errors) {
            this.loginError = 'El usuario o la contraseña son incorrectos.';
        } else {
            this.loginError = 'Ocurrió un error inesperado. Por favor, inténtalo de nuevo.';
        }
      }
    });
  }
}
