import Link from "next/link";
import { Menu } from "lucide-react";

import { Button } from "@/components/ui/button";
import { UserMenu } from "@/components/shared/user-menu";
import { getCurrentUser } from "@/lib/session";

export async function AdminTopbar() {
  const user = await getCurrentUser();

  return (
    <header className="flex h-16 items-center justify-between border-b border-border bg-background/80 px-4 backdrop-blur sm:px-6">
      <div className="flex items-center gap-3">
        <Button variant="ghost" size="icon" className="lg:hidden">
          <Menu className="h-5 w-5" />
        </Button>
        <Link href="/dashboard" className="text-sm text-muted-foreground hover:text-foreground">
          ← Student view
        </Link>
      </div>
      {user && <UserMenu name={user.name} email={user.email} image={user.image} role={user.role} />}
    </header>
  );
}
