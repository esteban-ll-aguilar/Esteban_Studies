import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, ActivatedRoute, Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Movie } from '../../models/movie.model';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator';
import { MatChipsModule } from '@angular/material/chips';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-movie-list',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    MatCardModule,
    MatButtonModule,
    MatProgressSpinnerModule,
    MatPaginatorModule,
    MatChipsModule,
    MatIconModule
  ],
  template: `
    <div class="container">
      <div class="header-container">
        <h1 class="page-title">{{ searchQuery ? 'Resultados de búsqueda' : 'Películas Populares' }}</h1>
        <mat-chip-listbox *ngIf="searchQuery">
          <mat-chip>
            Búsqueda: {{ searchQuery }}
            <mat-icon matChipRemove (click)="clearSearch()">cancel</mat-icon>
          </mat-chip>
        </mat-chip-listbox>
      </div>

      <div *ngIf="loading" class="loading-container">
        <mat-spinner></mat-spinner>
      </div>

      <div *ngIf="!loading && movies.length === 0" class="no-results">
        <h2>No se encontraron películas</h2>
        <p *ngIf="searchQuery">Intenta con otra búsqueda</p>
        <button mat-raised-button color="primary" (click)="clearSearch()">Ver películas populares</button>
      </div>      <div *ngIf="!loading && movies.length > 0" class="movie-grid">
        <mat-card *ngFor="let movie of movies" class="movie-card" (click)="goToMovieDetail(movie.id)">
          <img 
            mat-card-image 
            [src]="movieService.getImageUrl(movie.poster_path)" 
            [alt]="movie.title"
            class="movie-poster"
          >
          <mat-card-content>
            <div class="rating-badge">
              <span>{{ movie.vote_average | number:'1.1-1' }}</span>
            </div>
            <h2 class="movie-title">{{ movie.title }}</h2>
            <p class="release-date">{{ movie.release_date | date:'mediumDate' }}</p>
            <p class="movie-id">ID: {{ movie.id }}</p>
          </mat-card-content>
        </mat-card>
      </div>

      <mat-paginator 
        *ngIf="!loading && totalResults > 0"
        [length]="totalResults"
        [pageSize]="20"
        [pageIndex]="currentPage - 1"
        (page)="onPageChange($event)"
        aria-label="Seleccionar página">
      </mat-paginator>
    </div>
  `,
  styles: [`
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }
    .header-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
    }
    .page-title {
      font-size: 2rem;
      font-weight: 500;
      margin: 0;
    }
    .loading-container {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 300px;
    }
    .movie-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
    }
    .movie-card {
      display: flex;
      flex-direction: column;
      height: 100%;
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
      overflow: hidden;
      position: relative;
    }
    .movie-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    .movie-poster {
      height: 300px;
      object-fit: cover;
    }
    .movie-title {
      font-size: 1rem;
      margin: 10px 0 5px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }    .release-date {
      font-size: 0.9rem;
      color: rgba(0,0,0,0.6);
      margin: 0;
    }
    .movie-id {
      font-size: 0.8rem;
      color: rgba(0,0,0,0.5);
      margin-top: 5px;
    }
    .rating-badge {
      position: absolute;
      top: 10px;
      right: 10px;
      background-color: rgba(0,0,0,0.7);
      color: white;
      border-radius: 50%;
      width: 40px;
      height: 40px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-weight: bold;
    }
    .no-results {
      text-align: center;
      padding: 50px 0;
    }
    .no-results h2 {
      margin-bottom: 20px;
    }
  `]
})
export class MovieListComponent implements OnInit {
  movies: Movie[] = [];
  loading = true;
  currentPage = 1;
  totalResults = 0;
  searchQuery: string | null = null;
  constructor(
    public movieService: MovieService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.searchQuery = params['query'] || null;
      this.currentPage = +params['page'] || 1;
      this.loadMovies();
    });
  }

  loadMovies(): void {
    this.loading = true;
    
    if (this.searchQuery) {
      this.movieService.searchMovies(this.searchQuery, this.currentPage).subscribe({
        next: (response) => {
          this.movies = response.results;
          this.totalResults = response.total_results;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error searching movies', error);
          this.loading = false;
        }
      });
    } else {
      this.movieService.getPopularMovies(this.currentPage).subscribe({
        next: (response) => {
          this.movies = response.results;
          this.totalResults = response.total_results;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error fetching popular movies', error);
          this.loading = false;
        }
      });
    }
  }

  onPageChange(event: PageEvent): void {
    this.currentPage = event.pageIndex + 1;
    this.loadMovies();
  }
  clearSearch(): void {
    this.searchQuery = null;
    this.currentPage = 1;
    this.loadMovies();
  }

  goToMovieDetail(id: number): void {
    console.log(`Navigating to movie details with ID: ${id}`);
    this.router.navigate(['/movie', id]);
  }
}
