import type MeiliSearch from 'meilisearch';
import PocketBase from 'pocketbase';


// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
		interface Locals {
			pb: PocketBase
			ms: MeiliSearch
			user: AuthModel | null,
			settings: Settings | null

		}
	}
}

export { };
